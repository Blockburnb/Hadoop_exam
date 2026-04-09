from mrjob.job import MRJob


class MRTagUsage(MRJob):

    def mapper(self, _, line):

        try:

            parts = line.split(',')

            # Format : userId,movieId,tag,timestamp

            if parts[2] != 'tag':

                yield parts[2], 1

        except:

            pass


    def reducer(self, key, values):

        yield key, sum(values)


if __name__ == '__main__':

    MRTagUsage.run()
