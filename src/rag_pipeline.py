def run(self, query):

    print("Retrieving relevant incidents...")

    results = self.retriever.search(query)

    print("Building context...")

    context = self.context_builder.build_context(
        query,
        results
    )

    print("Generating report...")

    prompt = build_prompt(
        query,
        context
    )

    report = self.gemini.generate_report(
        prompt
    )

    return {
        "query": query,
        "retrieved_incidents": results,
        "context": context,
        "report": report
    }