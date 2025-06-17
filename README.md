# Ancient Wisdom Nostr Bot

A bot that posts random quotes from ancient philosophers to Nostr. The quotes are sourced from various ancient texts and compiled into a JSON format.

You can follow the bot on Nostr: `npub1sages7tvxdmmtu9gadt80dk2jzws767l30r6xntq39ffhrp0ytlsax9yar`

## Components

- `quotes.json`: The main database of quotes, containing both the quote text and author information
- `parse_quotes.py`: Script to parse quotes from text files into JSON format
- `combine_quotes.py`: Script to combine quotes from multiple sources into a single JSON file
- `post-random-quote.sh`: Script to post a random quote to Nostr

## Usage

### Adding New Quotes

1. Add new quotes to a text file in the format:
   ```
   "Quote text here."
   —Author Name
   ```

2. Use `parse_quotes.py` to convert the text file to JSON:
   ```bash
   python3 parse_quotes.py
   ```

3. Use `combine_quotes.py` to merge with existing quotes:
   ```bash
   python3 combine_quotes.py
   ```

### Posting Quotes

To post a random quote to Nostr:
```bash
./post-random-quote.sh
```

The output will be in the format:
```
"Quote text here." —Author Name
```

## Requirements

- Python 3
- `jq` command-line tool
- Nostr client configured with your keys

## License

MIT License 