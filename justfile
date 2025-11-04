default: run

# Install dependencies
install:
    uv sync

# Run the project
run:
    @uv run python src/main.py
