from mrjob.job import MRJob


class MRTagsPerUser(MRJob):

    def mapper(self, _, line):

        try:

            parts = line.split(',')

            if parts[0] != 'userId':

                yield parts[0], 1

        except:

            pass


    def reducer(self, key, values):

        yield key, sum(values)


if __name__ == '__main__':

    MRTagsPerUser.run()
