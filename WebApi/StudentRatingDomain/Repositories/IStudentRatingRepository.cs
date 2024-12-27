using StudentRatingDomain.Entities;

namespace StudentRatingDomain.Repositories
{
    public interface IStudentRatingRepository
    {
        public Task<IEnumerable<StudentRating>> GetCurrentStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<IEnumerable<StudentRating>> GetAfterRetakeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<IEnumerable<StudentRating>> GetCumulativeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<StudentRating> GetGraduateStudentRatingByNameAsync(string firstName, string lastName, string patronymic);
    }
}
