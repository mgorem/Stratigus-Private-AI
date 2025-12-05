# agent.py
import lmstudio as lms
from fetch_tool import fetch_webpage


def print_fragment(fragment, round_index: int = 0) -> None:
    """
    Stream partial assistant output as it arrives.
    The default round_index parameter keeps this compatible
    with other lmstudio calls.
    """
    print(fragment.content, end="", flush=True)


def main() -> None:
    # 1. Connecting to a local model exposed by LM Studio (Qwen 2.5-VL-7B Instruct)
    #    This identifier must match the model ID shown in LM Studio.
    #    For our case: we connected to "qwen2.5-vl-7b-instruct".
    model = lms.llm("qwen2.5-vl-7b-instruct")

    # 2. Create a chat context with instructions for tool use
    chat = lms.Chat(
        "You are a local web-analysis assistant running on the user's computer. "
        "When the user provides a URL or asks about a specific web page, "
        "first call the `fetch_webpage` tool to retrieve and read the page. "
        "Then, based on the user's request, summarise, analyse, or answer "
        "questions about that page."
    )

    # 3. Simple REPL loop
    while True:
        try:
            user_input = input("\nUser (Please prompt the tool to fetch and summarise a page of your choice or blank + Enter to exit): ")
        except EOFError:
            print()
            break

        if not user_input.strip():
            break

        chat.add_user_message(user_input)

        print("Assistant: ", end="", flush=True)

        # 4. Let the model decide when to call tools
        #    Here we expose the Python function as a tool.
        model.act(
            chat,
            [fetch_webpage],              # List of tools
            on_message=chat.append,       # Save final assistant messages to chat
            on_prediction_fragment=print_fragment,  # Stream output
        )

        print()  # newline after each answer


if __name__ == "__main__":
    main()
