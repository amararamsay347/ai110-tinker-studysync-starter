"""
StudySync -- Find a Study Spot (Ticket 3, Tinker 3B).

TICKET: none of the ranking logic is implemented yet -- every function
below is a stub.
"""

import csv

NOISE_ORDER = {"quiet": 0, "moderate": 1, "loud": 2}


def load_study_spots(csv_path: str) -> list:
    """
    Load study spots from a CSV into a list of dicts, converting
    "distance_miles" to float and "seats_available" to int.
    """
    # TODO: use csv.DictReader to read csv_path into a list of dicts.
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        spots = []
        for row in reader:
            # Convert distance_miles to float and seats_available to int
            row["distance_miles"] = float(row["distance_miles"])
            row["seats_available"] = int(row["seats_available"])
            spots.append(row)
    # TODO: convert row["distance_miles"] to float and row["seats_available"] to int for each row.
    for spot in spots:
        spot['distance_miles'] = float(spot['distance_miles'])
        spot['seats_available'] = int(spot['seats_available'])
    return spots

#print(load_study_spots("data/study_spots.csv"))


def score_study_spot(profile: dict, spot: dict) -> tuple:
    """
    Score one study spot against a student profile.

    profile example: {"max_noise": "moderate", "max_distance": 1.0, "min_seats": 4}

    Return (score, reasons) where reasons is a list of short strings
    explaining what contributed to the score, e.g. ["quiet enough", "close enough"].
    """
    score = 0.0
    reasons = []

    # Noise: compare levels using NOISE_ORDER.
    spot_noise = NOISE_ORDER[spot["noise_level"]]
    max_noise = NOISE_ORDER[profile["max_noise"]]
    if spot_noise <= max_noise:
        score += 2.0
        reasons.append("quiet enough")
        if spot_noise < max_noise:
            score += 0.5
            reasons.append("quieter than needed")
    else:
        score -= 2.0
        reasons.append("too noisy")

    # Distance: within the limit helps, beyond it hurts.
    if spot["distance_miles"] <= profile["max_distance"]:
        score += 2.0
        reasons.append("close enough")
    else:
        score -= 1.0
        reasons.append("too far")

    # Seats: enough seats helps, too few hurts.
    if spot["seats_available"] >= profile["min_seats"]:
        score += 1.0
        reasons.append("enough seats")
    else:
        score -= 1.0
        reasons.append("not enough seats")

    return score, reasons
#Test against spots in the csv
profile = {"max_noise": "moderate", "max_distance": 1.0, "min_seats": 4}
spots = load_study_spots("data/study_spots.csv")
for spot in spots:
    print(spot["name"], score_study_spot(profile, spot))


def rank_study_spots(profile: dict, spots: list, k: int = 3) -> list:
    """
    Score every study spot, then return the top k as (spot, score, reasons)
    tuples, sorted by score descending.
    """
    # TODO: score every spot with score_study_spot(), then use
    # sorted(..., key=..., reverse=True)[:k] to keep only the top k.
    ranking = []
    for spot in spots:
        score, reasons = score_study_spot(profile, spot)
        ranking.append((spot, score, reasons))
    return sorted(ranking, key=lambda x: x[1], reverse=True)[:k]
print(rank_study_spots(profile, spots, k=3))

def format_results(ranked: list) -> None:
    """Print each ranked study spot with its score and reasons, one line each."""
    # TODO: for each (spot, score, reasons) tuple, print a readable line, e.g.:
    # "1. Innovation Commons -- Score: 5.0 -- Because: quiet enough, close enough"
    for i, (spot, score, reasons) in enumerate(ranked, start=1):
        print(f"{i}. {spot['name']} -- Score: {score:.1f} -- Because: {', '.join(reasons)}")
    raise NotImplementedError


def render_study_spot_tab():
    import streamlit as st

    st.subheader("Find a Study Spot")
    max_noise = st.selectbox("Max noise level", ["quiet", "moderate", "loud"], index=1)
    max_distance = st.slider("Max distance (miles)", 0.0, 3.0, 1.0)
    min_seats = st.number_input("Minimum seats needed", min_value=1, value=4, step=1)

    if st.button("Find spots"):
        profile = {"max_noise": max_noise, "max_distance": max_distance, "min_seats": min_seats}
        try:
            spots = load_study_spots("data/study_spots.csv")
            ranked = rank_study_spots(profile, spots, k=3)
            for spot, score, reasons in ranked:
                st.write(f"**{spot['name']}** -- Score: {score:.1f} -- Because: {', '.join(reasons)}")
        except NotImplementedError:
            st.warning("🚧 Ranking isn't implemented yet -- that's Tinker 3B's ticket.")


if __name__ == "__main__":
    spots = load_study_spots("data/study_spots.csv")
    profile = {"max_noise": "moderate", "max_distance": 1.0, "min_seats": 4}
    ranked = rank_study_spots(profile, spots, k=3)
    format_results(ranked)
