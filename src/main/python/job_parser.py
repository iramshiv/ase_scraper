def home_job_parser(job_to_parse):
    job_split = job_to_parse.split()
    words_in_job = len(job_split)
    word_array_length = words_in_job - 1
    word = 0
    temp_word = ''
    while word < word_array_length:
        split_word = job_split[word] + "+"
        temp_word = temp_word + split_word
        word += 1
    parse_job = temp_word + job_split[word_array_length]
    return parse_job


def other_job_parser(job_to_parse):
    job_split = job_to_parse.split()
    words_in_job = len(job_split)
    word_array_length = words_in_job - 1
    word = 0
    temp_word = ''
    while word < word_array_length:
        split_word = job_split[word] + "%20"
        temp_word = temp_word + split_word
        word += 1
    parse_job = temp_word + job_split[word_array_length]
    return parse_job
