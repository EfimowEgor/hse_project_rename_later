using MySql.Data.MySqlClient;
using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;

namespace StudentRatingDataAccess
{
    public sealed class StudentRepository(string connectionString) : IStudentRepository
    {
        public async Task<bool> HasStudentAsync(Student student)
        {
            var query = "SELECT EXISTS(SELECT 1 FROM Students WHERE Name = @Name AND Surname = @Surname AND Patronymic = @Patronymic)";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Name", student.FirstName);
            command.Parameters.AddWithValue("@Surname", student.LastName);
            command.Parameters.AddWithValue("@Patronymic", student.Patronymic);

            var hasStudent = await command.ExecuteScalarAsync();
            return Convert.ToBoolean(hasStudent);
        }


        public async Task<IEnumerable<Student>> GetStudentsByFirstNameAsync(string firstName)
        {
            var query = "SELECT Surname, Patronymic FROM Students WHERE Name = @Name ORDER BY Surname, Patronymic";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Name", firstName);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var lastName = reader.GetString(0);
                var patronymic = reader.GetString(1);

                students.Add(new(firstName, lastName, patronymic));
            }

            return students;
        }

        public async Task<IEnumerable<Student>> GetStudentsByLastNameAsync(string lastName)
        {
            var query = "SELECT Name, Patronymic FROM Students WHERE Surname = @Surname ORDER BY Name, Patronymic";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Surname", lastName);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var firstName = reader.GetString(0);
                var patronymic = reader.GetString(1);

                students.Add(new(firstName, lastName, patronymic));
            }

            return students;
        }

        public async Task<IEnumerable<Student>> GetStudentsByPatronymicAsync(string patronymic)
        {
            var query = "SELECT Name, Surname FROM Students WHERE Patronymic = @Patronymic ORDER BY Surname, Name";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Patronymic", patronymic);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var firstName = reader.GetString(0);
                var lastName = reader.GetString(1);

                students.Add(new(firstName, lastName, patronymic));
            }

            return students;
        }
    }
}
