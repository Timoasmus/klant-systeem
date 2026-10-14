import pandas as pd 
from agent_core.tools.agent_tools import db_agent
from pathlib import Path

HERE = Path(__file__).parent
tests = pd.read_excel(HERE / "db_agent_test.xlsx")

for i, (_, test) in enumerate(tests.iterrows()):
    print(f"{i + 1}/{len(tests)}: {test['Vraag']}")

    antwoord = db_agent.chat(
        [],
        user_prompt=test["Vraag"]
    )[-1]["content"]

    tests.loc[i, "Resultaat"] = antwoord
    tests.to_excel(HERE / "db_agent_test_results.xlsx", index=False)