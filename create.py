start = 1
end = 1
for i in range(1, 65536):
    if i % 500 == 1:
        start = i
        end = i + 499 if i + 499 < 65536 else 65535
        with open(f"Port-description{start}-{end}.md", "w", encoding="utf-8") as f:
            for j in range(start, end + 1):
                f.write(f"## Port {j}\n")
                f.write(f"### Description\n")
                f.write(f"### Common uses\n")
                f.write(f"### Security considerations\n")
                f.write(f"---\n")
