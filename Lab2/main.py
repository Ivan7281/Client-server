from fastapi import FastAPI, Query

app = FastAPI()

def find_phone_number(text: str):
    phone_numbers = []
    text_length = len(text)

    i = 0
    while i < text_length:
        if text[i:i+6] == "+38095" or text[i:i+6] == "+38050" or text[i:i+6] == "+38066":
            if i+13 <= text_length:
                phone_numbers.append(text[i:i+13])
            i += 13
        else:
            i += 1
    return phone_numbers


@app.get("/find_phone_number/")
async def get_phone_number(text: str = Query(..., title="Text")):
    phone_numbers = find_phone_number(text)
    return {"phone_numbers": phone_numbers}
