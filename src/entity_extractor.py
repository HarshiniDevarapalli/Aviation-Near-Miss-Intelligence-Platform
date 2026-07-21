import re
import spacy


class EntityExtractor:
    """
    Extracts aviation entities from an incident report.
    """

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.operations = [
            "taxi",
            "takeoff",
            "landing",
            "approach",
            "departure",
            "climb",
            "descent",
            "pushback"
        ]

        self.weather = [
            "fog",
            "rain",
            "snow",
            "ice",
            "wind",
            "gust",
            "storm",
            "turbulence"
        ]

    def extract(self, incident):

        text = incident["document"]

        doc = self.nlp(text)

        entities = {
            "airports": [],
            "aircraft": [],
            "operations": [],
            "weather": [],
            "primary_problem": incident["metadata"].get("primary_problem"),
            "contributing_factors": incident["metadata"].get(
                "contributing_factors"
            ),
            "result": incident["metadata"].get("result")
        }

        # Named entities

        for ent in doc.ents:

            if ent.label_ == "GPE":
                entities["airports"].append(ent.text)

        # Aircraft (simple regex)

        aircraft = re.findall(
            r"\b[A-Z]{1,3}\d{2,4}\b",
            text
        )

        entities["aircraft"] = list(set(aircraft))

        # Operations

        lower = text.lower()

        for op in self.operations:

            if op in lower:
                entities["operations"].append(op)

        # Weather

        for w in self.weather:

            if w in lower:
                entities["weather"].append(w)

        return entities