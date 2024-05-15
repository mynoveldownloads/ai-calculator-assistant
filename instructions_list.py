def list_of_instructions(user_input):
    if ('median') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example:
        user input: what is the median of variable abc? give me the median of variable abc.
        system output: median(abc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "median of abc" just reply median(abc) and do not explain or elaborate any further.
        """
        return output
    elif ('mean') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example:
        user input: what is the mean of variable abc? give me the mean of variable abc.
        system output: mean(abc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "mean of abc" just reply mean(abc) and do not explain or elaborate any further.
        """
        return output

    elif ('sd') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example:
        user input: what is the sd of variable abc? give me the sd of variable abc.
        system output: SD_population(abc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "sd of abc" just reply SD_population(abc) and do not explain or elaborate any further.
        """
        return output

    elif ('variance') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example:
        user input: what is the variance of variable abc? give me the variance of abc.
        system output: variance_population(abc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "variance of abc" just reply variance_population(abc) and do not explain or elaborate any further.
        """

        return output
    elif ('sum') in user_input:
        output = """
        Follow instructions properly. dont reply anything else but the system output template. if there are multiple variables, print it in commas
        Example:
        user input: what is the sum of variable abc? give me the sum of abc.
        system output: sum(abc)
        Answer nothing else but the system output given in the example.
        Note: if user asks "sum of abc" just reply sum(abc) and do not explain or elaborate any further.
                """

        return output
    else:
        return 'None'
