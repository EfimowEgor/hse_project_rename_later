using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;
using StudentRatingDomain.Services;

namespace StudentRatingServices
{
    public sealed class StudentRatingService(IStudentRatingRepository studentRatingRepository) : IStudentRatingService
    {
        public async Task<IEnumerable<StudentRating>> GetCurrentStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            return await studentRatingRepository.GetCurrentStudentRatingsByNameAsync(firstName, lastName, patronymic);
        }

        public async Task<IEnumerable<StudentRating>> GetAfterRetakeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            return await studentRatingRepository.GetAfterRetakeStudentRatingsByNameAsync(firstName, lastName, patronymic);
        }

        public async Task<IEnumerable<StudentRating>> GetCumulativeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            return await studentRatingRepository.GetCumulativeStudentRatingsByNameAsync(firstName, lastName, patronymic);
        }

        public async Task<StudentRating> GetGraduateStudentRatingByNameAsync(string firstName, string lastName, string patronymic)
        {
            return await studentRatingRepository.GetGraduateStudentRatingByNameAsync(firstName, lastName, patronymic);
        }
    }
}
