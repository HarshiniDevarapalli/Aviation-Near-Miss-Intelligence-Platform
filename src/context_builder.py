class ContextBuilder:
    """
    Builds structured context from retrieved incidents
    before sending it to the LLM.
    """

    def build_context(self, query: str, retrieved_results: list) -> str:

        context = []

        context.append("=" * 80)
        context.append("AVIATION INCIDENT CONTEXT")
        context.append("=" * 80)
        context.append(f"\nUser Query:\n{query}\n")

        context.append("Retrieved Historical Incidents\n")

        for idx, result in enumerate(retrieved_results, start=1):

            metadata = result["metadata"]

            incident = f"""
Incident {idx}
----------------------------------------
Incident ID: {result["id"]}

Date:
{metadata.get("date","Unknown")}

Primary Problem:
{metadata.get("primary_problem","Unknown")}

Contributing Factors:
{metadata.get("contributing_factors","Unknown")}

Result:
{metadata.get("result","Unknown")}

Narrative:
{result["document"]}

Similarity Distance:
{result["distance"]:.4f}

----------------------------------------
"""

            context.append(incident)

        return "\n".join(context)