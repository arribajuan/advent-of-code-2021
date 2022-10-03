https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test?source=recommendations

dotnet new sln -o AOC2021.Day6

cd AOC2021.Day6

dotnet new classlib -o LanternFishService
dotnet sln add ./LanternFishService/LanternFishService.csproj

dotnet new xunit -o LanternFishService.Tests
dotnet sln add ./LanternFishService.Tests/LanternFishService.Tests.csproj

dotnet add ./LanternFishService.Tests/LanternFishService.Tests.csproj reference ./LanternFishService/LanternFishService.csproj




dotnet new sln -o AOC2021.Day6
cd AOC2021.Day6
dotnet new classlib -o LanternFishService
ren .\LanternFishService\Class1.cs LanternFishService.cs
dotnet sln add ./LanternFishService/LanternFishService.csproj
dotnet new xunit -o LanternFishService.Tests
dotnet add ./LanternFishService.Tests/LanternFishService.Tests.csproj reference ./LanternFishService/LanternFishService.csproj
dotnet sln add ./LanternFishService.Tests/LanternFishService.Tests.csproj

Add 
  <ItemGroup>
    <None Include="$(SolutionDir)Inputs\**" CopyToOutputDirectory="PreserveNewest" LinkBase="Inputs\" />
  </ItemGroup>

to .TEsts.csproj


