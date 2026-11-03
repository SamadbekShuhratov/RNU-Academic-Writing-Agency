# RNU-Academic-Writing-Agency

This repository implements the **RNU Autonomous Academic Writing Agency** with:

- Complete thesis markdown deliverable using the RNU 3-Arrow Logic:
  - `/home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/thesis_undergraduate.md`
- Executable LangGraph-based 8-employee orchestrator:
  - `/home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/src/rnu_agency.py`
- Team installation/configuration file:
  - `/home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/.installed.json`
- Google Sheets and Gmail integration instructions:
  - `/home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/docs/google_integrations.md`

## Quick Run
```bash
python /home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/src/rnu_agency.py \
  --topic "Autonomous RNU Thesis Generation" \
  --output /home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/generated_thesis.md
```
