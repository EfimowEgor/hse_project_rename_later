using StudentRatingDomain.Entities;

namespace StudentRatingDomain.Services
{
    public interface IStudentService
    {
        public Task<bool> HasStudentAsync(string name, string surname, string patronymic);

        public Task<IEnumerable<Student>> GetStudentsByIncompleteNameAsync(string partName);

        public Task<IEnumerable<Student>> GetStudentsByIncompleteNameAsync(string partName1, string partName2); 
    }
}
