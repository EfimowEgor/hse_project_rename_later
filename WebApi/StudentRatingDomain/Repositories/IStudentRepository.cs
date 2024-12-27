using StudentRatingDomain.Entities;

namespace StudentRatingDomain.Repositories
{
    public interface IStudentRepository
    {
        public Task<bool> HasStudentAsync(string firstName, string lastName, string patronymic);

        public Task<IEnumerable<Student>> GetStudentsByFirstNameAsync(string firstName);

        public Task<IEnumerable<Student>> GetStudentsByLastNameAsync(string lastName);

        public Task<IEnumerable<Student>> GetStudentsByPatronymicAsync(string patronymic);
    }
}
