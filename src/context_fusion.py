class ContextFusion:
    """
    Combines semantic retrieval results with graph retrieval
    into a single context for the LLM.
    """

    def build_context(
        self,
        semantic_context,
        graph_context
    ):

        context = []

        context.append("=" * 80)
        context.append("SEMANTIC EVIDENCE")
        context.append("=" * 80)
        context.append("")

        context.append(semantic_context)

        context.append("")
        context.append("=" * 80)
        context.append("GRAPH RELATIONSHIPS")
        context.append("=" * 80)
        context.append("")

        for item in graph_context:

            context.append(
                f"Node: {item['node']}"
            )

            context.append(
                f"Similarity: {item['score']:.3f}"
            )

            context.append("Connected Entities:")

            for neighbor in item["neighbors"]:

                context.append(
                    f"  • {neighbor}"
                )

            context.append("")

        return "\n".join(context)