def color_score(top, bottom, shoes):
    score = 0

    colors = {
        "white": ["black", "blue", "beige", "white"],
        "black": ["white", "blue", "beige", "black"],
        "blue": ["white", "black", "beige", "blue"],
        "beige": ["white", "black", "blue", "beige"]
    }

    if bottom["color"] in colors.get(top["color"], []):
        score += 3

    if shoes["color"] in colors.get(bottom["color"], []):
        score += 2

    return score


def style_score(top, bottom, shoes):
    score = 0

    if top["style"] == bottom["style"]:
        score += 3

    if bottom["style"] == shoes["style"]:
        score += 2

    return score


def formality_score(top, bottom, shoes):
    difference_1 = abs(
        top["formality"] - bottom["formality"]
    )

    difference_2 = abs(
        bottom["formality"] - shoes["formality"]
    )

    score = 5

    score -= difference_1
    score -= difference_2

    return max(score, 0)


def occasion_score(top, bottom, shoes, occasion):
    score = 0

    formality = (
        top["formality"]
        + bottom["formality"]
        + shoes["formality"]
    ) / 3

    if occasion == "College":

        if formality <= 2:
            score += 3

    elif occasion == "Casual":

        if formality <= 2:
            score += 3

    elif occasion == "Formal":

        if formality >= 3:
            score += 3

    return score


def season_score(top, bottom, shoes, season):
    score = 0

    items = [top, bottom, shoes]

    for item in items:

        if "all" in item["season"]:
            score += 1

        elif season.lower() in item["season"]:
            score += 2

    return score


def total_score(
    top,
    bottom,
    shoes,
    occasion="College",
    season="Summer"
):

    color = color_score(
        top,
        bottom,
        shoes
    )

    style = style_score(
        top,
        bottom,
        shoes
    )

    formality = formality_score(
        top,
        bottom,
        shoes
    )

    occasion_points = occasion_score(
        top,
        bottom,
        shoes,
        occasion
    )

    season_points = season_score(
        top,
        bottom,
        shoes,
        season
    )

    return (
        color
        + style
        + formality
        + occasion_points
        + season_points
    )

def explain_outfit(top, bottom, shoes, occasion, season):
    reasons = []

    if top["color"] == bottom["color"]:
        reasons.append("The top and bottom use a coordinated color family.")
    else:
        reasons.append(
            f"{top['color'].title()} works well with {bottom['color']}."
        )

    if bottom["color"] == shoes["color"]:
        reasons.append("The shoes match the bottom for a consistent look.")
    else:
        reasons.append(
            f"{shoes['color'].title()} shoes complement the outfit."
        )

    if top["style"] == bottom["style"]:
        reasons.append(
            f"The pieces share a {top['style']} style."
        )

    average_formality = (
        top["formality"]
        + bottom["formality"]
        + shoes["formality"]
    ) / 3

    if occasion == "Formal" and average_formality >= 3:
        reasons.append("The outfit's formality matches the occasion.")

    elif occasion in ["College", "Casual"] and average_formality <= 2:
        reasons.append("The outfit has an appropriate relaxed formality.")

    if "all" in top["season"] or season.lower() in top["season"]:
        reasons.append(f"The outfit is suitable for {season.lower()}.")

    return reasons


class reasons:
    """Generate human-readable reasons for an outfit recommendation."""

    def explain(self, top, bottom, shoes, occasion, season):
        """Return explanations using the same rules as the scoring functions."""
        return explain_outfit(top, bottom, shoes, occasion, season)

    def color(self, top, bottom, shoes):
        """Return the color-related explanations for an outfit."""
        result = []
        if top["color"] == bottom["color"]:
            result.append("The top and bottom use a coordinated color family.")
        else:
            result.append(
                f"{top['color'].title()} works well with {bottom['color']}."
            )

        if bottom["color"] == shoes["color"]:
            result.append("The shoes match the bottom for a consistent look.")
        else:
            result.append(
                f"{shoes['color'].title()} shoes complement the outfit."
            )
        return result

    def formality(self, top, bottom, shoes, occasion):
        """Return an explanation when the outfit fits the occasion."""
        average = (
            top["formality"] + bottom["formality"] + shoes["formality"]
        ) / 3
        if occasion == "Formal" and average >= 3:
            return "The outfit's formality matches the occasion."
        if occasion in ("College", "Casual") and average <= 2:
            return "The outfit has an appropriate relaxed formality."
        return None

    def season(self, top, bottom, shoes, season):
        """Return an explanation when at least one item suits the season."""
        if any(
            "all" in item["season"] or season.lower() in item["season"]
            for item in (top, bottom, shoes)
        ):
            return f"The outfit is suitable for {season.lower()}."
        return None