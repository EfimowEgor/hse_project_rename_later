using StudentRatingDomain.Entities;

namespace StudentRatingDomain.Services
{
    public interface IStudentRatingService
    {
        public Task<IEnumerable<StudentRating>> GetCurrentStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<IEnumerable<StudentRating>> GetAfterRetakeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<IEnumerable<StudentRating>> GetCumulativeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic);

        public Task<StudentRating> GetGraduateStudentRatingByNameAsync(string firstName, string lastName, string patronymic);
    }
}
