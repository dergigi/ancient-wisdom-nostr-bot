import json

def read_quotes_from_txt():
    quotes = []
    current_quote = None
    current_author = None
    quote_number = 1

    with open('quotes.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Start of a quote with curly quote
        if not current_quote and line.startswith('"'):
            current_quote = line[1:-1]  # Remove the quotes
            # Look ahead for author
            j = i + 1
            while j < len(lines):
                author_line = lines[j].strip()
                if author_line:
                    if author_line.startswith('—'):
                        current_author = author_line[1:].strip()
                        quotes.append({
                            "n": quote_number,
                            "quote": current_quote,
                            "author": current_author
                        })
                        quote_number += 1
                        current_quote = None
                        current_author = None
                    break
                j += 1
            i = j
        else:
            i += 1

    return quotes

def read_quotes_from_json():
    with open('new_quotes.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def combine_quotes():
    # Read quotes from both sources
    txt_quotes = read_quotes_from_txt()
    json_quotes = read_quotes_from_json()
    
    # Combine all quotes
    all_quotes = txt_quotes + json_quotes
    
    # Renumber quotes sequentially
    for i, quote in enumerate(all_quotes, 1):
        quote['n'] = i
    
    # Save to quotes.json with proper UTF-8 encoding
    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(all_quotes, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    combine_quotes() 