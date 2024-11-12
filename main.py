import argparse
import logging
from faker import Faker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_text(count: int) -> list[str]:
    fake = Faker()
    return [fake.text() for _ in range(count)]


def main():
    parser = argparse.ArgumentParser(description="Generate random text")
    parser.add_argument("--count", type=int, default=1, help="Number of texts to generate")
    args = parser.parse_args()

    texts = generate_text(args.count)
    for text in texts:
        logger.info(text)


if __name__ == "__main__":
    main()
