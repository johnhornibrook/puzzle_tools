
import math

class FrequencyAnalysis:
    """
    Collection of tools to determine whether or not a string is likely to be english.
    Can be used for other languages if a suitable frequency distribution is found.
    """
    
    non_existent_gram_score = 0.5
    
    def __init__(self, quadgram_path='english_quadgrams.txt'):
        self.quadgrams = {}
        self.total_quadgram_count = 0
        self._load_dictionary(quadgram_path)

    def score_string(self, s):
        """
        Log probability of how likely this string is to be english.
        It's the sum of the individual quadgram probabilities divided by the number of quadgrams 
        involved. That is, it can be compared to scores of strings of different length
        """
        s = self._clean_string(s)

        score = 0
        for i in range(len(s) - 3):
            quadgram = s[i:i+4]
            score += self._score_gram(quadgram)
        return score / (len(s) - 3)

    def rank_strings(self, s_array, num_to_output=10):
        """
        Ranks a list of strings by how likely they are to be english, and prints out the top few
        """
        
        string_score_pairs = []
        for s in s_array:
            string_score_pairs.append((s, self.score_string(s)))
        string_score_pairs.sort(key = lambda x: -x[1])
        for n in range(num_to_output):
            print(string_score_pairs[n][0], round(string_score_pairs[n][1], 1))


    def _load_dictionary(self, quadgram_path):
        with open(quadgram_path, 'r') as f:
            for line in f:
                separated = line.split()
                quad = separated[0].lower()
                count = int(separated[1])
                self.quadgrams[quad] = count
                self.total_quadgram_count += count

    def _score_gram(self, quad):
        """
        Log probability of how likely a quadgram is to be english.
        Specifically, it's the log likelihood of a randomly sampled english quadgram to be exactly this
        """
        n = self.quadgrams[quad] if quad in self.quadgrams else self.non_existent_gram_score
        return math.log(n / self.total_quadgram_count)
    
    def _clean_string(self, s):
        """
        Removes everything that isn't letters in a string and converts to lower case
        """
        f = filter(str.isalpha, s)
        s = "".join(f)
        return s.lower()

    