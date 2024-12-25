using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;

namespace StudentRatingDataAccess
{
    public sealed class StudentRepository : IStudentRepository
    {
        private static readonly IReadOnlyList<Student> _students = GetAllStudents();


        public async Task<bool> HasStudentAsync(Student student)
        {
            return await Task.Run(() => _students.Any(s => s.Equals(student)));
        }


        public async Task<IEnumerable<Student>> GetStudentsByFirstNameAsync(string firstName)
        {
            return await Task.Run(() => _students.Where(s => s.FirstName == firstName));
        }

        public async Task<IEnumerable<Student>> GetStudentsByLastNameAsync(string lastName)
        {
            return await Task.Run(() => _students.Where(s => s.LastName == lastName));
        }

        public async Task<IEnumerable<Student>> GetStudentsByPatronymicAsync(string patronymic)
        {
            return await Task.Run(() => _students.Where(s => s.Patronymic == patronymic));
        }


        private static IReadOnlyList<Student> GetAllStudents()
        {
            return [new("Егор", "Ефимов", "Александрович"),
                new("Егор", "Эщэщ", "Эщэщович"),
                new("Александр", "Ивакин", "Дмитриевич"),
                new("Александр", "Эщэщ", "Дмитриевич"),
                new("Александр", "Эщэщ", "Эщэщович")];
        }
    }
}
