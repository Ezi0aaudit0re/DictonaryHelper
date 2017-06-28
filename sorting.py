__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

from operator import itemgetter

class DictionarySorting:
    def convertToList(self, dict={}):
        """
        This function breaks down a a dictionary into an array of keys and values and then uses zip method to convert it
        into an array of tuples. It updates the tuple_format variable
        :param dict: dictionary to convert
        :return: list - a list filled with tupples
        """
        keys, values = dict.keys(), dict.values()
        list = zip(keys, values)
        return list

    def convertToDictionary(self, list = zip()):
        """
        Takes in a list of tuples and converts it to dictionary
        :param list:
        :return: sorted dictionary
        """
        dict = {}
        for a, b in list:
            dict[a] = b
        return dict

    def sorting(self, dict={}):
        """
        This function takes in a dictionary and sorts it in asseding order
        :param dict: dictionary to sort
        :return: a sorted dictionary
        """
        list = self.convertToList(dict)
        list = sorted(list, key = lambda t:t[1])
        return self.convertToDictionary(list)


    def sortingList(self,list = [],param1 = None,param2 = None,method='asc'):
        """
        This function takes in a list of dictionary and sorts it in asseding order
        :param list: dictionary to sort
        :param param1: parameter to sort it by
        :param param2: second parameter to sort it by
        :param method: desc to sort in descending order
        :return: a sorted dictionary
        """
        params = itemgetter(param1) if param2 == None else itemgetter(param1, param2)
        return sorted(list, key=params, reverse=False if method == 'asc' else True)

    def max(self, dict={}, orderBy="value"):
        """
        Returns the maximum value in the dictionary
        :param dict: dictionary to find the maximum value
        :param orderBy: find by key or value
        :return: maximum in the form of a dictionary based on the orderBy provided
        """
        list = zip()
        if orderBy.lower() == "value":
            list = max(zip(dict.values(), dict.keys()))
            return {list[1]: list[0]}
        elif orderBy.lower() == "key":
            list = max(zip(dict.keys(), dict.values()))
            return {list[0]: list[1]}
        else:
            pass




    def min(self, dict={}, orderBy="value"):
        """
        Returns the minimum value in the dictionary
        :param dict: dictionary to find the minimum value
        :param orderBy: find by key or value
        :return: minimum in the form of a dictionary based on the orderBy provided
        """
        list = zip()
        if orderBy.lower() == "value":
            list = min(zip(dict.values(), dict.keys()))
            return {list[1]: list[0]}
        elif orderBy.lower() == "key":
            list = min(zip(dict.keys(), dict.values()))
            return {list[0]: list[1]}

        else:
            pass

# dict = DictionarySorting().sortingList(stocks, "price", "name")
# print(dict)