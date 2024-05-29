import openai 

def get_car_ai_bio(model, brand, year): 
    prompt = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas do modelo.
    ''' 
    openai.api_key = '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' 
    prompt = prompt.format(brand, model, year) 
    response = openai.completions.create( 
        model="gpt-3.5-turbo-instruct", 
        prompt=prompt, 
        max_tokens=1000 ) 
    return response.choices[0].text