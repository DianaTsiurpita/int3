"""Train the model and persist the resulting artifact."""

from pathlib import Path

import joblib
from sklearn.metrics import mean_absolute_error, r2_score

from .model import (
    CAT,
    NUM,
    TARGET,
    load_training_data,
    train_model,
)


ARTIFACTS = (
    Path(__file__).resolve().parent.parent
    / "artifacts"
)


def main() -> None:
    """Train the model, report metrics, and persist the artifact."""

    df = load_training_data()

    model = train_model()

    predictions = model.predict(
        df[NUM + CAT]
    )

    r2 = r2_score(
        df[TARGET],
        predictions,
    )

    mae = mean_absolute_error(
        df[TARGET],
        predictions,
    )

    print(
        f"[train] Ames in-sample: "
        f"R2={r2:.4f}, MAE={mae:.0f} USD"
    )

    ARTIFACTS.mkdir(
        parents=True,
        exist_ok=True,
    )

    artifact_path = ARTIFACTS / "model.pkl"

    joblib.dump(
        model,
        artifact_path,
    )

    print(
        f"[train] artifact persisted: {artifact_path}"
    )


if __name__ == "__main__":
    main()
