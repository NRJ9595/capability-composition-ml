from .main import load_application, find_capability
from .embedding import encode_capability, cosine_similarity
from .compatibility import are_compatible
from .composition import compose_capabilities


def run_experiments():
    """
    Run the main experiments for the capability-composition study.
    """

    _, goal, capabilities = load_application()

    create_order = find_capability(
        capabilities, "CreateOrder"
    )

    make_payment = find_capability(
        capabilities, "MakePayment"
    )

    send_notification = find_capability(
        capabilities, "SendNotification"
    )

    cancel_cart = find_capability(
        capabilities, "CancelCart"
    )

    send_email = find_capability(
        capabilities, "SendEmailConfirmation"
    )

    print("=" * 60)
    print("FORMAL EXPERIMENTS")
    print("=" * 60)

    # ---------------------------------------------------------
    # Experiment 1: Compatible capability pairs
    # ---------------------------------------------------------

    print()
    print("Experiment 1: Compatible capability pairs")

    compatible_pairs = [
        (create_order, make_payment),
        (make_payment, send_notification),
    ]

    for first, second in compatible_pairs:
        result = are_compatible(first, second)

        print(
            f"{first.name} -> {second.name}: "
            f"{result}"
        )

    # ---------------------------------------------------------
    # Experiment 2: Incompatible capability pair
    # ---------------------------------------------------------

    print()
    print("Experiment 2: Incompatible capability pair")

    result = are_compatible(
        create_order,
        cancel_cart
    )

    print(
        f"CreateOrder -> CancelCart: "
        f"{result}"
    )

    # ---------------------------------------------------------
    # Experiment 3: Alternative implementations
    # ---------------------------------------------------------

    print()
    print("Experiment 3: Alternative implementations")

    notification_vector = encode_capability(
        send_notification
    )

    email_vector = encode_capability(
        send_email
    )

    similarity = cosine_similarity(
        notification_vector,
        email_vector
    )

    print(
        "SendNotification <-> "
        f"SendEmailConfirmation: "
        f"{similarity:.4f}"
    )

    # ---------------------------------------------------------
    # Experiment 4: Capability composition
    # ---------------------------------------------------------

    print()
    print("Experiment 4: Capability composition")

    sequence = [
        create_order,
        make_payment,
        send_notification,
    ]

    composite = compose_capabilities(sequence)

    print(
        f"Composite: {composite.name}"
    )

    print(
        f"Cost: {composite.cost:.4f}"
    )

    print(
        f"Reliability: "
        f"{composite.reliability:.4f}"
    )

    print(
        f"Availability: "
        f"{composite.availability:.4f}"
    )

    # ---------------------------------------------------------
    # Experiment 5: Goal achievement
    # ---------------------------------------------------------

    print()
    print("Experiment 5: Goal achievement")

    goal_achieved = True

    for key, required_value in goal.conditions.items():

        produced_value = composite.effects.get(key)

        if produced_value != required_value:
            goal_achieved = False

        print(
            f"{key}: "
            f"required={required_value}, "
            f"produced={produced_value}"
        )

    print(
        f"Goal achieved: {goal_achieved}"
    )

    print()
    print("=" * 60)


if __name__ == "__main__":
    run_experiments()
