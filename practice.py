#print('Hello World!')

def word_count(text: str) -> dict:
    text = text.lower()
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def get_top_students(students, threshold):
    result = []
    for student in students:
        name = student.get("name", "")
        scores = student.get("scores", [])
        if scores:
            avg = sum(scores) / len(scores)
        else:
            avg = 0
        if avg >= threshold:
            result.append((name, avg))
    result.sort(key=lambda x: x[1], reverse=True)
    return [name for name, _ in result]


if __name__ == "__main__":
    text = "Sampoerna IT Internship Program is amazing amazing IT IT"
    print(word_count(text))

    students = [
        {"name": "Andi",  "scores": [80, 90, 75]},
        {"name": "Brina", "scores": [60, 70]},
        {"name": "Cindy", "scores": [90, 95, 85, 100]},
        {"name": "Doni",  "scores": []},
    ]
    print(get_top_students(students, 80))

