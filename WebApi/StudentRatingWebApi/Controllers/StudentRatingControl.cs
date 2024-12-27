using AutoMapper;
using Microsoft.AspNetCore.Mvc;
using StudentRatingDomain.Services;
using StudentRatingWebApi.Dtos;

namespace StudentRatingWebApi.Controllers
{
    [ApiController]
    [Route("students/ratings")]
    public sealed class StudentRatingControl(IMapper mapper, IStudentRatingService studentRatingService) : ControllerBase
    {
        [HttpGet("current")]
        public async Task<ActionResult<IEnumerable<StudentRatingDto>>> GetCurrentStudentRatingsByNameAsync([FromQuery] string firstName,
            [FromQuery] string lastName,
            [FromQuery] string patronymic)
        {
            var ratings = await studentRatingService.GetCurrentStudentRatingsByNameAsync(firstName, lastName, patronymic);
            var ratingDtos = mapper.Map<IEnumerable<StudentRatingDto>>(ratings);

            return Ok(ratingDtos);
        }

        [HttpGet("after_retake")]
        public async Task<ActionResult<IEnumerable<StudentRatingDto>>> GetAfterRetakeStudentRatingsByNameAsync([FromQuery] string firstName,
            [FromQuery] string lastName,
            [FromQuery] string patronymic)
        {
            var ratings = await studentRatingService.GetAfterRetakeStudentRatingsByNameAsync(firstName, lastName, patronymic);
            var ratingDtos = mapper.Map<IEnumerable<StudentRatingDto>>(ratings);

            return Ok(ratingDtos);
        }

        [HttpGet("cumulative")]
        public async Task<ActionResult<IEnumerable<StudentRatingDto>>> GetCumulativeStudentRatingsByNameAsync([FromQuery] string firstName,
            [FromQuery] string lastName,
            [FromQuery] string patronymic)
        {
            var ratings = await studentRatingService.GetCumulativeStudentRatingsByNameAsync(firstName, lastName, patronymic);
            var ratingDtos = mapper.Map<IEnumerable<StudentRatingDto>>(ratings);

            return Ok(ratingDtos);
        }

        //[HttpGet("graduate")]
        //public async Task<ActionResult<StudentRatingDto>> GetGraduateStudentRatingByNameAsync([FromQuery] string firstName,
        //    [FromQuery] string lastName,
        //    [FromQuery] string patronymic)
        //{
        //    try
        //    {
        //        var rating = await studentRatingService.GetGraduateStudentRatingByNameAsync(firstName, lastName, patronymic);
        //        var ratingDto = mapper.Map<StudentRatingDto>(rating);
        //        return Ok(ratingDto);
        //    }
        //    catch
        //    {
        //        return NotFound();
        //    }
        //}
    }
}
