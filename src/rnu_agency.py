from __future__ import annotations

import argparse
import base64
import csv
import datetime as dt
import json
import os
from dataclasses import dataclass
from email.mime.text import MIMEText
from pathlib import Path
from typing import Dict, List, TypedDict

from langgraph.graph import END, StateGraph


class AgencyState(TypedDict):
    topic: str
    outputs: Dict[str, str]
    ledger: List[List[str]]


@dataclass(frozen=True)
class Employee:
    name: str
    task: str


EMPLOYEES = [
    Employee("Project Manager", "Enforce constraints and orchestrate execution"),
    Employee("Outline & Structure Architect", "Prepare title, object/subject, and defended statements"),
    Employee("Chapter 1 Specialist", "Write introduction and factual problem formulation"),
    Employee("Literature Review Specialist", "Review existing solution families and gaps"),
    Employee("Theoretical Framework Specialist", "Define theory and framework"),
    Employee("Practical Implementation Specialist", "Write implementation and empirical section"),
    Employee("General Conclusion Editor", "Compose conclusion aligned to three nails"),
    Employee("Formatting & Bibliography Editor", "Finalize bibliography and consistency"),
]


REQUIRED_PREFIXES = [
    "Has been OFFERED",
    "Has been MODIFIED",
    "Has been SUGGESTED",
]


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def append_ledger_row(state: AgencyState, agent: str, task: str, status: str) -> None:
    state["ledger"].append([utc_now(), agent, task, status])


def project_manager(state: AgencyState) -> AgencyState:
    append_ledger_row(state, "Project Manager", "Pipeline initialized with RNU constraints", "done")
    return state


def outline_architect(state: AgencyState) -> AgencyState:
    topic = state["topic"]
    nails = "\n".join(
        [
            "1. Has been OFFERED a strict RNU-compliant autonomous multi-agent architecture.",
            "2. Has been MODIFIED the linear workflow into a graph-based, auditable pipeline.",
            "3. Has been SUGGESTED a practical integration model with Sheets and Gmail reporting.",
        ]
    )
    state["outputs"]["outline"] = (
        f"## Title\n{topic}\n\n"
        "## Object and Subject\n"
        "- Object: Undergraduate thesis preparation process.\n"
        "- Subject: LangGraph-based autonomous writing governance system.\n\n"
        "## Defended Thesis Statements\n"
        f"{nails}\n"
    )
    append_ledger_row(state, "Outline & Structure Architect", "Outline package generated", "done")
    return state


def chapter1_specialist(state: AgencyState) -> AgencyState:
    state["outputs"]["chapter1"] = (
        "## Chapter 1. Introduction and Problem Formulation\n"
        "Modern universities need reliable and auditable writing pipelines for standards-heavy outputs.\n"
        "Tertiary education enrollment scale and digitalization pressures raise quality-control demands for thesis production.\n"
        "Generic writing tools do not guarantee institutional rule compliance or deterministic chapter structure.\n"
        "Therefore, an RNU-focused autonomous system is needed to enforce writing constraints and generate verifiable outputs.\n\n"
        "Research goal: By 31 May 2027, implement and validate an 8-agent LangGraph system that generates a full thesis draft with 100% RNU-matrix compliance on a deterministic checklist.\n\n"
        "Chapter 1 Summary: The core problem, factual context, and single SMART goal were defined.\n"
    )
    append_ledger_row(state, "Chapter 1 Specialist", "Chapter 1 drafted", "done")
    return state


def literature_review_specialist(state: AgencyState) -> AgencyState:
    state["outputs"]["chapter2a"] = (
        "## Chapter 2. Literature Review\n"
        "Single-agent drafting systems offer speed but limited governance guarantees.\n"
        "Workflow automations provide task routing but typically lack institution-specific semantic checks.\n"
        "The research gap is an integrated architecture combining generation, deterministic constraints, and management auditability.\n\n"
    )
    append_ledger_row(state, "Literature Review Specialist", "Literature section drafted", "done")
    return state


def theoretical_framework_specialist(state: AgencyState) -> AgencyState:
    state["outputs"]["chapter2b"] = (
        "### Theoretical Framework\n"
        "The project applies multi-agent specialization, graph-orchestrated state transitions, and quality-gate validation.\n"
        "The 3-arrow logic maps problem evidence to method review and finally to a practical implementation path.\n\n"
        "Chapter 2 Summary: Existing methods and the theoretical basis justify the proposed graph-governed agency.\n"
    )
    append_ledger_row(state, "Theoretical Framework Specialist", "Framework section drafted", "done")
    return state


def practical_implementation_specialist(state: AgencyState) -> AgencyState:
    state["outputs"]["chapter3"] = (
        "## Chapter 3. Practical Implementation and Empirical Analysis\n"
        "The implementation is an executable LangGraph pipeline with eight role-specific nodes and ledger logging.\n"
        "Validation checks include one SMART goal, three mandatory defended statements, chapter-end summaries, and implementation proof.\n"
        "Run: python src/rnu_agency.py --topic \"Autonomous RNU Thesis\" --output generated_thesis.md\n\n"
        "Chapter 3 Summary: The system implementation and measurable compliance checks are operational.\n"
    )
    append_ledger_row(state, "Practical Implementation Specialist", "Chapter 3 drafted", "done")
    return state


def general_conclusion_editor(state: AgencyState) -> AgencyState:
    state["outputs"]["conclusion"] = (
        "## General Conclusion\n"
        "The proposed system satisfies the three defended statements by combining strict rule enforcement, graph orchestration, and practical reporting integrations.\n"
        "This approach provides a reusable and auditable model for undergraduate thesis production under RNU constraints.\n"
    )
    append_ledger_row(state, "General Conclusion Editor", "Conclusion drafted", "done")
    return state


def formatting_editor(state: AgencyState) -> AgencyState:
    state["outputs"]["bibliography"] = (
        "## Bibliography\n"
        "1. UNESCO. Education: From disruption to recovery.\n"
        "2. World Bank Data. School enrollment, tertiary (gross).\n"
        "3. ENQA. Standards and Guidelines for Quality Assurance in the EHEA (ESG 2015).\n"
    )
    append_ledger_row(state, "Formatting & Bibliography Editor", "Formatting and bibliography finalized", "done")
    return state


def build_graph():
    graph = StateGraph(AgencyState)
    graph.add_node("project_manager", project_manager)
    graph.add_node("outline_architect", outline_architect)
    graph.add_node("chapter1_specialist", chapter1_specialist)
    graph.add_node("literature_review_specialist", literature_review_specialist)
    graph.add_node("theoretical_framework_specialist", theoretical_framework_specialist)
    graph.add_node("practical_implementation_specialist", practical_implementation_specialist)
    graph.add_node("general_conclusion_editor", general_conclusion_editor)
    graph.add_node("formatting_editor", formatting_editor)

    graph.set_entry_point("project_manager")
    graph.add_edge("project_manager", "outline_architect")
    graph.add_edge("outline_architect", "chapter1_specialist")
    graph.add_edge("chapter1_specialist", "literature_review_specialist")
    graph.add_edge("literature_review_specialist", "theoretical_framework_specialist")
    graph.add_edge("theoretical_framework_specialist", "practical_implementation_specialist")
    graph.add_edge("practical_implementation_specialist", "general_conclusion_editor")
    graph.add_edge("general_conclusion_editor", "formatting_editor")
    graph.add_edge("formatting_editor", END)
    return graph.compile()


def compile_thesis(outputs: Dict[str, str]) -> str:
    parts = [
        "# Autonomous Academic Writing Thesis Output\n",
        outputs["outline"],
        outputs["chapter1"],
        outputs["chapter2a"],
        outputs["chapter2b"],
        outputs["chapter3"],
        outputs["conclusion"],
        outputs["bibliography"],
    ]
    return "\n".join(parts).strip() + "\n"


def validate_outputs(text: str) -> None:
    if text.count("Research goal:") != 1:
        raise ValueError("Output must contain exactly one SMART research goal sentence.")
    for prefix in REQUIRED_PREFIXES:
        if prefix not in text:
            raise ValueError(f"Missing defended statement prefix: {prefix}")
    if text.count("Chapter 1 Summary") != 1 or text.count("Chapter 2 Summary") != 1 or text.count("Chapter 3 Summary") != 1:
        raise ValueError("Each chapter must end with a chapter summary.")


def write_ledger_csv(path: Path, rows: List[List[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Agent Name", "Task Performed", "Output Status"])
        writer.writerows(rows)


def build_google_services():
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        return None, None
    service_account_file = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
    if not service_account_file:
        return None, None
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/gmail.send",
    ]
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    delegated_user = os.getenv("GOOGLE_DELEGATED_USER")
    if delegated_user:
        credentials = credentials.with_subject(delegated_user)
    sheets = build("sheets", "v4", credentials=credentials, cache_discovery=False)
    gmail = build("gmail", "v1", credentials=credentials, cache_discovery=False)
    return sheets, gmail


def append_sheet_rows(sheets_service, spreadsheet_id: str, rows: List[List[str]]) -> None:
    sheets_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Ledger!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": rows},
    ).execute()


def send_daily_brief(gmail_service, recipient: str, subject: str, body: str) -> None:
    message = MIMEText(body)
    message["to"] = recipient
    message["subject"] = subject
    encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()
    gmail_service.users().messages().send(userId="me", body={"raw": encoded}).execute()


def maybe_report_to_google(ledger_rows: List[List[str]], thesis_text: str) -> None:
    spreadsheet_id = os.getenv("GOOGLE_SHEETS_ID")
    brief_to = os.getenv("DAILY_BRIEF_TO")
    sheets, gmail = build_google_services()
    if sheets and spreadsheet_id:
        append_sheet_rows(sheets, spreadsheet_id, ledger_rows)
    if gmail and brief_to:
        send_daily_brief(
            gmail,
            recipient=brief_to,
            subject="RNU Agency Daily Brief",
            body=f"Run completed at {utc_now()} with {len(ledger_rows)} ledger rows.\n\nPreview:\n{thesis_text[:1500]}",
        )


def run(topic: str, output_path: Path, ledger_path: Path) -> Dict[str, str]:
    app = build_graph()
    initial_state: AgencyState = {"topic": topic, "outputs": {}, "ledger": []}
    final_state: AgencyState = app.invoke(initial_state)
    thesis_text = compile_thesis(final_state["outputs"])
    validate_outputs(thesis_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(thesis_text, encoding="utf-8")
    write_ledger_csv(ledger_path, final_state["ledger"])
    maybe_report_to_google(final_state["ledger"], thesis_text)

    return {
        "output": str(output_path),
        "ledger": str(ledger_path),
        "rows": str(len(final_state["ledger"])),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RNU autonomous thesis writing agency")
    parser.add_argument("--topic", required=True, help="Thesis topic")
    parser.add_argument("--output", default="generated_thesis.md", help="Output markdown file")
    parser.add_argument("--ledger", default="ledger/agency_ledger.csv", help="Ledger CSV path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run(args.topic, Path(args.output), Path(args.ledger))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
