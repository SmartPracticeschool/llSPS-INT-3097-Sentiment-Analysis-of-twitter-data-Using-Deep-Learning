from textblob import TextBlob

pos_count = 0
neg_count = 0
i = 0
with open("dataset.csv","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity >= 0.1:
            pos_count +=1
        if analysis.sentiment.polarity <= -0.1:
            neg_count +=1
        i +=1
        print(i)
        if i>=10000:
            break

neutral = i-(pos_count+neg_count)

print('Positive = ',pos_count)
print('Negative = ',neg_count)
print('Neutral = ', abs(neutral))
