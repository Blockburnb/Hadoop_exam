from mrjob.job import MRJob


class MRTagsPerMovie(MRJob):

    def mapper(self, _, line):

        try:

            parts = line.split(',')

            if parts[1] != 'movieId':

                yield parts[1], 1

        except:

            pass


    def reducer(self, key, values):

        yield key, sum(values)


if __name__ == '__main__':

    MRTagsPerMovie.run()
