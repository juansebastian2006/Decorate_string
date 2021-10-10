def decorate(s: str) -> str:
    words = s.upper().split()
    return ("  ".join(" _" * len(w) for w in words) +
            "\n|" +"| |".join('|'.join(list(w)) for w in words) +
            "|\n" + "  ".join(" ‾" * len(w) for w in words)
           )
    
