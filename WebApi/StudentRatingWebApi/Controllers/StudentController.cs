using AutoMapper;
using Microsoft.AspNetCore.Mvc;
using StudentRatingDomain.Services;
using StudentRatingWebApi.Dtos;

namespace StudentRatingWebApi.Controllers
{
    [ApiController]
    [Route("students")]
    public class StudentController(IMapper mapper, IStudentService studentService) : ControllerBase
    {
        [HttpGet("has")]
        public async Task<ActionResult<bool>> HasStudentAsync([FromQuery] string firstName, 
            [FromQuery] string lastName,
            [FromQuery] string patronymic)
        {
            var hasStudent = await studentService.HasStudentAsync(firstName, lastName, patronymic);
            return Ok(hasStudent);
        }

        [HttpGet("one_part_name")]
        public async Task<ActionResult<IEnumerable<StudentDto>>> GetStudentsByIncompleteNameAsync([FromQuery] string partName)
        {
            var students = await studentService.GetStudentsByIncompleteNameAsync(partName);
            var studentDtos = mapper.Map<IEnumerable<StudentDto>>(students);
            return Ok(studentDtos);
        }

        [HttpGet("two_parts_name")]
        public async Task<ActionResult<IEnumerable<StudentDto>>> GetStudentsByIncompleteNameAsync([FromQuery] string partName1,
            [FromQuery] string partName2)
        {
            var students = await studentService.GetStudentsByIncompleteNameAsync(partName1, partName2);
            var studentDtos = mapper.Map<IEnumerable<StudentDto>>(students);
            return Ok(studentDtos);
        }
    }
}
