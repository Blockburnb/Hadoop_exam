from mrjob.job import MRJob


class MRUserTagsPerMovie(MRJob):

    def mapper(self, _, line):

        try:

            parts = line.split(',')

            if parts[0] != 'userId':

                # On cree une clef "movieId,userId"

                # parts[1] est le movieId, parts[0] est le userId

                key = parts[1] + "," + parts[0]

                yield key, 1

        except:

            pass


    def reducer(self, key, values):

        yield key, sum(values)


if __name__ == '__main__':

    MRUserTagsPerMovie.run()
