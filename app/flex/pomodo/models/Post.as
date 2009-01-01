package pomodo.models {
  import org.ruboss.collections.ModelsCollection;
  import org.ruboss.models.RubossModel;
  
  [Resource(name="posts")]
  [Bindable]
  public class Post extends RubossModel {
    public static const LABEL:String = "title";

    public var title:String;

    public var content:String;

    [HasMany]
    public var comments:ModelsCollection;
    
    public function Post() {
      super(LABEL);
    }
  }
}
