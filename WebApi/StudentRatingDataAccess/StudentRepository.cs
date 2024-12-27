using MySql.Data.MySqlClient;
using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;

namespace StudentRatingDataAccess
{
    public sealed class StudentRepository(string connectionString) : IStudentRepository
    {
        public async Task<bool> HasStudentAsync(string firstName, string lastName, string patronymic)
        {
            var query = "SELECT EXISTS(SELECT 1 FROM Students WHERE Name = @Name AND Surname = @Surname AND Patronymic = @Patronymic)";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Name", firstName);
            command.Parameters.AddWithValue("@Surname", lastName);
            command.Parameters.AddWithValue("@Patronymic", patronymic);

            var hasStudent = await command.ExecuteScalarAsync();
            return Convert.ToBoolean(hasStudent);
        }


        public async Task<IEnumerable<Student>> GetStudentsByFirstNameAsync(string firstName)
        {
            var query = "SELECT Id, Surname, Patronymic FROM Students WHERE Name = @Name ORDER BY Surname, Patronymic";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Name", firstName);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var id = reader.GetInt32(0);
                var lastName = reader.GetString(1);
                var patronymic = reader.GetString(2);

                students.Add(new(id, firstName, lastName, patronymic));
            }

            return students;
        }

        public async Task<IEnumerable<Student>> GetStudentsByLastNameAsync(string lastName)
        {
            var query = "SELECT Id, Name, Patronymic FROM Students WHERE Surname = @Surname ORDER BY Name, Patronymic";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Surname", lastName);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var id = reader.GetInt32(0);
                var firstName = reader.GetString(1);
                var patronymic = reader.GetString(2);

                students.Add(new(id, firstName, lastName, patronymic));
            }

            return students;
        }

        public async Task<IEnumerable<Student>> GetStudentsByPatronymicAsync(string patronymic)
        {
            var query = "SELECT Id, Name, Surname FROM Students WHERE Patronymic = @Patronymic ORDER BY Surname, Name";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Patronymic", patronymic);

            var students = new List<Student>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var id = reader.GetInt32(0);
                var firstName = reader.GetString(1);
                var lastName = reader.GetString(2);

                students.Add(new(id, firstName, lastName, patronymic));
            }

            return students;
        }
    }
}
