from seminar7.domain import SingerStatsDTO


class PerformanceService:
    def __init__(self, performance_repo):
        self.__repo = performance_repo

    def get_concerts_for_singer(self, singer):
        results = []
        for performance in self.__repo.get_all():
            if performance.get_singer() == singer:
                results.append(performance.get_concert())
        return results

    def get_singer_stats(self):
        """
        For each singer the number of concerts they attended
        :return:
        """
        all_singers = set(
            [performance.get_singer() for performance in self.__repo.get_all()]
        )
        results = {}
        for singer in all_singers:
            results[singer] = self.get_concerts_for_singer(singer)

        final_results = []
        for singer, nr_concerts in results.items():
            final_results.append(SingerStatsDTO(singer.get_name(), nr_concerts))
        return final_results
