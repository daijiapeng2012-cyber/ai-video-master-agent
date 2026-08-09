.PHONY: validate weekly

validate:
	python3 scripts/validate_knowledge_base.py

weekly:
	python3 scripts/generate_weekly_digest.py --date $${DATE:-2026-08-09}
