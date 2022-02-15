#smartbot-v0.1
#author - hungrychicken412



context = r"""
No, the valuations you receive from Flippa are free, and you can use the tool as many times as you like.
Flippa has more historical sales data than anyone else 
and is the largest marketplace globally for buying and selling sites, stores, apps and online businesses. 
If the information you provide is accurate, your Flippa valuation will be a good indicator of price.
Flippa uses your inputs and compares data to 1000's of similar sites that have sold on Flippa. 
We look at business model, category, age and many other factors. We also consider how many buyers are interested in sites like yours.
If you wish to list your online store for sale, or chat to us about your business, 
you can either start selling here or send a note to our team at AccountManager@Flippa.com. 
We'd be happy to provide some additional guidance.

"""

#LEVEL 2 OF THE BOT
from transformers import pipeline, Conversation
from sentence_transformers import SentenceTransformer, util

sentenceAnalyzer = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')
faq_model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"#"deepset/roberta-base-squad2"
question_answerer = pipeline(model=faq_model_name, task="question-answering")
faq = pipeline("question-answering")
#conversational_pipeline = pipeline("conversational")



class Bots:
    def __init__(self, questions, context):
        self.conv1 = Conversation("Hi there!")
        #self.out = conversational_pipeline([self.conv1])
        self.questions = questions
        self.context = context
        #print(self.out)
      
    def computeSimilarity(self, query):
        self.query = query

        query_emb = sentenceAnalyzer.encode(self.query)
        doc_emb = sentenceAnalyzer.encode(self.questions)

        scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

        doc_score_pairs = list(zip(self.questions, scores))
        score = max(scores)
        index = scores.index(score)
        

        return score, self.questions[index]#, max(doc_score_pairs)
      
    def ask_faq(self, question):
        return question_answerer(question=question, context=self.context)
    
    #def converse(self, msg):
        #self.conv1.add_user_input(msg)
        #self.out = conversational_pipeline([self.conv1])
        #return self.out



questions = ['do you like dogs?', 'do we have to go?']

similarity_threshold = 0.8
faq_threshold = 0.1

class smartbot:
    def __init__(self, questions, context, similarity_threshold,faq_threshold):
        self.similarity_threshold = similarity_threshold
        self.faq_threshold = faq_threshold
        self.context = context
        self.bots = Bots(questions, context)

    def process_message(self, message, questionDict):
        reply = ''
        similarity = self.bots.computeSimilarity(message)
        reply = similarity[1]
        #print(similarity)

        if (similarity[0] < self.similarity_threshold):
          faq = self.bots.ask_faq(message)
          #reply = faq['answer']
          try:
              reply = questionDict[faq['answer']]
          except:
              pass
          #print(faq)

          #if (faq['score'] < self.faq_threshold):
            #conv = self.bots.converse(message)
            #print(conv)
        
        return reply
            
        
          
if __name__ == "__main__":
    b = smartbot(questions, context, similarity_threshold, faq_threshold)
    #print(b.process_message("how do I sell my business?"))
    while 1:
        ans = b.process_message(str(input(">> ")))
        print(ans)
