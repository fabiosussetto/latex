require "rubygems"
require "rspec"
require "watir-webdriver"

describe "My Web Application" do
  let(:browser) { @browser ||= Watir::Browser.new :chrome }

  before { browser.goto "http://example.com" }
  after  { browser.close }

  it "should login user" do
    browser.text_field(:name => "username").set "user" 
    browser.text_field(:id => "password").set "test"
    browser.button.click
    browser.h2.text.should == "You are logged in"
  end
end