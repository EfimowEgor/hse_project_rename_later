using StudentRatingDataAccess;
using StudentRatingDomain.Repositories;
using StudentRatingDomain.Services;
using StudentRatingServices;

namespace StudentRatingWebApi
{
    internal class Startup(IConfiguration configuration)
    {
        public IConfiguration Configuration => configuration;


        public void ConfigureServices(IServiceCollection services)
        {
            services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());

            var connectionString = Configuration.GetConnectionString("StudentMySqlDb");

            services.AddScoped<IStudentRepository>(_ => new StudentRepository(connectionString!));
            services.AddScoped<IStudentRatingRepository>(_ => new StudentRatingRepository(connectionString!));

            services.AddScoped<IStudentService, StudentService>();
            services.AddScoped<IStudentRatingService, StudentRatingService>();

            services.AddControllers();
            services.AddEndpointsApiExplorer();
            services.AddSwaggerGen();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.UseHttpsRedirection();
            app.UseRouting();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
