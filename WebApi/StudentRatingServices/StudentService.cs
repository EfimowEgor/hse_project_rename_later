using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;
using StudentRatingDomain.Services;

namespace StudentRatingServices
{
    public sealed class StudentService(IStudentRepository studentRepository) : IStudentService
    {
        public async Task<bool> HasStudentAsync(string firstName, string lastName, string patronymic)
        {
            return await studentRepository.HasStudentAsync(firstName, lastName, patronymic);
        }

        public async Task<IEnumerable<Student>> GetStudentsByIncompleteNameAsync(string partName)
        {
            var studentsByFirst = await studentRepository.GetStudentsByFirstNameAsync(partName);
            var studentsByLastName = await studentRepository.GetStudentsByLastNameAsync(partName);
            var studentsByPatronymic = await studentRepository.GetStudentsByPatronymicAsync(partName);

            var result = studentsByFirst.Union(studentsByLastName).Union(studentsByPatronymic);
            return result;
        }

        public async Task<IEnumerable<Student>> GetStudentsByIncompleteNameAsync(string partName1, string partName2)
        {
            var students1 = await GetStudentsByIncompleteNameAsync(partName1);
            var students2 = await GetStudentsByIncompleteNameAsync(partName2);

            var result = students1.Intersect(students2);
            return result;
        }
    }
}
