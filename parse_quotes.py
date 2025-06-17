import json

def parse_quotes():
    quotes = []
    quote_number = 1
    in_quote = False
    quote_lines = []
    current_author = None

    with open('book.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Start of a quote with curly quote
        if not in_quote and line.startswith('“'):
            in_quote = True
            quote_lines = [line[1:]] if len(line) > 1 else []
            # If quote ends on the same line
            if line.endswith('”') and len(line) > 1:
                quote_lines[-1] = quote_lines[-1][:-1]
                in_quote = False
        elif in_quote:
            # End of quote
            if line.endswith('”'):
                quote_lines.append(line[:-1])
                in_quote = False
            else:
                quote_lines.append(line)
        elif not in_quote and quote_lines:
            # After quote, look for author
            while i < len(lines):
                author_line = lines[i].strip()
                if author_line.startswith('—'):
                    current_author = author_line[1:].strip()
                    quote = ' '.join([l for l in quote_lines if l])
                    quotes.append({
                        "n": quote_number,
                        "quote": quote,
                        "author": current_author
                    })
                    quote_number += 1
                    quote_lines = []
                    current_author = None
                    break
                i += 1
        i += 1

    with open('new_quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, indent=4)

if __name__ == "__main__":
    parse_quotes() 