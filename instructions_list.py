
# Instructions are fine-tuned for phi3:instruct, may not work for other models
# llama3:instruct can also be used but will give wrong outputs for some tasks e.g median of multiple vars

# NOTE: keep instructions short (not more than 10 sentences) else wrong output
def list_of_instructions(user_input):
    if ('median') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example 1:
        user input: what is the median of variable abc? give me the median of variable abc. find abc median
        system output: median(abc)
        
        
        Answer nothing else but the system output given in the example.
        Note: if user asks "median of abc" just reply median(abc) and do not explain or elaborate any further.
        """
        # Example 2:
        #         user input: what is the median of variable aaa bbb and ccc?
        #         system output: median(aaa), median(bbb), median(ccc)
        return output
    elif (('mean')in user_input):
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        "avg" or "average" in user input refers to the mean() function
        Example 1:
        user input: what is the mean of variable abc? give me the mean of variable abc. find abc mean
        system output: mean(abc)
        
        Note: if user asks "mean of abc" just reply mean(abc) and do not explain or elaborate any further.
        """
        # Example 2:
        #         user input: what is the mean of variable aaa bbb and ccc?
        #         system output: mean(aaa), mean(bbb), mean(ccc)
        return output

    elif (('sd') in user_input):
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        SD refers to standard deviation. use the SD_population() function
        Example 1:
        user input: what is the sd of variable abc? give me the sd of variable abc. find abc sd
        system output: SD_population(abc)
        Note: if user asks "sd of abc" just reply SD_population(abc) and do not explain or elaborate any further.
        """
        # Example 2:
        #         user input: what is the sd of variable aaa bbb and ccc?
        #         system output: SD_population(aaa), SD_population(bbb), SD_population(ccc)
        #         Answer nothing else but the system output given in the example.
        return output

    elif ('variance') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example 1:
        user input: what is the variance of variable abc? give me the variance of abc. find abc variance
        system output: variance_population(abc)
        
        Example 2:
        user input: what is the variance of variable aaa bbb and ccc?
        system output: variance_population(aaa), variance_population(bbb), variance_population(ccc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "variance of abc" just reply variance_population(abc) and do not explain or elaborate any further.
        """
        #
        #         Example 2:
        #         user input: what is the variance of variable aaa bbb and ccc?
        #         system output: variance_population(aaa), variance_population(bbb), variance_population(ccc)
        #         Answer nothing else but the system output given in the example.

        return output
    elif ('sum') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example 1:
        user input: what is the sum of variable abc? give me the sum of abc. find abc sum
        system output: sum(abc)

        Answer nothing else but the system output given in the example.
        Note: if user asks "sum of abc" just reply sum(abc) and do not explain or elaborate any further.
                """
        #
        #         Example 2:
        #         user input: what is the sum of variable aaa bbb and ccc?
        #         system output: sum(aaa), sum(bbb), sum(ccc)

        return output
    else:
        return 'None'

def prompt_formatting(prompt_input):
    formatted_text = prompt_input.lower().split()
    keyword_list = ['median', 'mean', 'sd', 'variance', 'sum']
    keyword = ''
    for i in range(len(keyword_list)):
        if keyword_list[i] in formatted_text:
            keyword += keyword_list[i]
            break
    if keyword in formatted_text:
        if (formatted_text[0] != keyword and formatted_text[0] != 'find'):
            formatted_text.insert(0, 'find')
            return ' '.join(formatted_text)
        elif formatted_text[0] == keyword:
            formatted_text.insert(0, 'find')
            return ' '.join(formatted_text)
        else:
            return ' '.join(formatted_text)
    else:
        return ' '.join(formatted_text)

def keyword(prompt_input):
    formatted_text = prompt_input.lower().split()
    keyword_list = ['median', 'mean', 'sd', 'variance', 'sum']
    keyword = ''
    for i in range(len(keyword_list)):
        if keyword_list[i] in formatted_text:
            keyword += keyword_list[i]
            break
    if keyword == 'sd':
        return 'standard deviation'
    else:
        return keyword
