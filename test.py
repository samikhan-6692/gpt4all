from gpt4all import GPT4All

model = GPT4All("ggml-gpt4all-j-v1.3-groovy")

output = model.generate("Hello, kaise ho?")
print(output)
