from typing import Any, Dict
from dataclasses import asdict

from .model import SheetConfig
from .utils import normalize_value, extract_lang, slugify


def build_front_matter(row: Dict[str, Any], mapping: SheetConfig | Dict[str, Any]) -> tuple[dict, dict]:
    """Build EN/EL front matter. Accepts either a dict mapping or a SheetConfig dataclass."""
    # Normalize mapping to a plain dict so we can safely call .get
    if not isinstance(mapping, dict):
        mapping = asdict(mapping)

    fm_en, fm_el = {}, {}
    defaults = mapping.get("defaults", {}) or {}
    fm_en.update(defaults)
    fields = mapping.get("fields", {}) or {}
    for excel_col, fm_key in fields.items():
        val = normalize_value(row.get(excel_col, None))
        base_key, lang = extract_lang(excel_col)
        if lang in (None, "en"):
            if val is not None:
                fm_en[fm_key] = val
        elif lang == "el":
            if val is not None:
                fm_el[fm_key] = val
    return fm_en, fm_el


def pick_slug(row: Dict[str,Any], mapping: SheetConfig | Dict[str,Any]) -> str:
    """Pick a stable slug, honoring an explicit slug field when provided.
    Accepts either a dict mapping or a SheetConfig dataclass.
    """
    # Normalize mapping to a plain dict so we can safely call .get
    if not isinstance(mapping, dict):
        mapping = asdict(mapping)

    slug_field = mapping.get("slug_field") or "slug"
    sv = row.get(slug_field, None)
    if sv is not None:
        s = str(sv).strip()
        if s and s.lower() != "nan":
            return slugify(s)

    fn = str(row.get("first_name", "") or "").strip()
    ln = str(row.get("last_name", "") or "").strip()
    if fn or ln:
        return slugify(f"{fn}-{ln}".strip("-"))

    for c in ["title.en", "title", "name.en", "name", "id"]:
        if c in row and row[c]:
            s = str(row[c]).strip()
            if s:
                return slugify(s)

    import hashlib
    return slugify("item-" + hashlib.md5(str(row).encode()).hexdigest()[:8])