input_path = 'data/rockyou.txt'
output_path = 'data/rockyou_clean.txt'

with open(input_path, 'r', encoding='utf-8', errors='ignore') as f_in:
    with open(output_path, 'w', encoding='ascii') as f_out:
        for line in f_in:
            # Remove non-ASCII characters and trim whitespace
            cleaned = line.encode('ascii', 'ignore').decode().strip()
            if cleaned:  # Skip empty lines
                f_out.write(cleaned + '\n')